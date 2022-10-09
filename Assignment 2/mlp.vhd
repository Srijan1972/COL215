library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity mlp is
    port(
        clk:in std_logic;
        start:in std_logic;
        disp:out std_logic_vector(6 downto 0);
        an:out std_logic_vector(3 downto 0));
end mlp;

architecture beh of mlp is
component comparator is
    port(
        cin:in std_logic_vector(15 downto 0);
        cout:out std_logic_vector(15 downto 0));
end component;

component counter is 
	generic (
		count_width : integer := 1);
	port(
		clk : in std_logic;
        clk_div : out std_logic);
end component;

component mac is
    port (
        clk:in std_logic;
        ctrl:in std_logic;
        en:in std_logic;
        din1 :in std_logic_vector(7 downto 0); -- to be read from ROM
        din2 :in std_logic_vector(15 downto 0); -- to be read from RAM
        dout :out std_logic_vector(15 downto 0));
end component;

component ram is
    port (
        clk :in std_logic;
        w   :in std_logic;
        din :in std_logic_vector(15 downto 0);
        addr:in std_logic_vector(9 downto 0);
        dout:out std_logic_vector(15 downto 0));
end component;

component rom is
    generic(
        img_file:string;
        params_file:string);
    port(
        clk:in std_logic;
        addr:in std_logic_vector(15 downto 0);
        dout:out std_logic_vector(7 downto 0));
end component;

component seven_seg is
    port(
        inp :in std_logic_vector(3 downto 0);
        disp:out std_logic_vector(6 downto 0);
        an  :out std_logic_vector(3 downto 0));
end component;

component shifter is
    port(
        sin:in std_logic_vector(15 downto 0);
        sout:out std_logic_vector(15 downto 0));
end component;
    signal cin:std_logic_vector(15 downto 0):=(others => '0');
    signal cout:std_logic_vector(15 downto 0):=(others => '0');
    signal clk_div:std_logic:='1';
    signal ctrl:std_logic:='0';
    signal mac_en:std_logic:='0';
    signal mac_din1:std_logic_vector(7 downto 0):=(others => '0');
    signal mac_din2:std_logic_vector(15 downto 0):=(others => '0');
    signal mac_dout:std_logic_vector(15 downto 0):=(others => '0');
    signal ram_w:std_logic:='0';
    signal ram_din:std_logic_vector(15 downto 0):=(others => '0');
    signal ram_addr:std_logic_vector(9 downto 0):=(others => '0');
    signal ram_dout:std_logic_vector(15 downto 0):=(others => '0');
    signal rom_addr:std_logic_vector(15 downto 0):=(others => '0');
    signal rom_dout:std_logic_vector(7 downto 0):=(others => '0');
    signal inp:std_logic_vector(3 downto 0):=X"F";
    signal sin:std_logic_vector(15 downto 0):=(others => '0');
    signal sout:std_logic_vector(15 downto 0):=(others => '0');
    signal ram_int:integer range 0 to 1023;
    signal rom_int:integer range 0 to 65535;
    signal iter_layer1:integer range 0 to 64;
    signal iter_layer2:integer range 0 to 10;
    signal bias1:integer range 0 to 65535:=51199;
    signal bias2:integer range 0 to 65535:=51903;
    signal write_counter:integer range 0 to 3:=0;
    type state_type is (beg,romtoram0,ror_dummy,romtoram1,start_layer1,mult_layer1,mult_inc1,load_bias1,wait_bias1,add_layer1,relu_layer1,write_layer1,dummy_layer1,back_layer1,start_layer2,mult_layer2,mult_inc2,load_bias2,wait_bias2,add_layer2,write_layer2,dummy_layer2,back_layer2,ready_for_max,wait_max,iter_max,set_max,inc_max,done);
    signal state:state_type:=beg;
    signal next_state:state_type:=beg;
    signal max_idx:integer range 0 to 15:=15;
    signal max_weight:std_logic_vector(15 downto 0):=X"8000";
    signal gt:std_logic:='0';
begin
    state <= next_state;
    ram_addr <= std_logic_vector(to_unsigned(ram_int,10));
    rom_addr <= std_logic_vector(to_unsigned(rom_int,16));
    relu:comparator port map(cin,cout);
    deter:counter port map(clk,clk_div);
    apple:mac port map(clk,ctrl,mac_en,mac_din1,mac_din2,mac_dout);
    local:ram port map(clk,ram_w,ram_din,ram_addr,ram_dout);
    global:rom generic map("imgdata_digit5.mif","weights_bias.mif") port map(clk,rom_addr,rom_dout);
    div:shifter port map(sin,sout);
    display:seven_seg port map(inp,disp,an);
    process(clk)
    begin
        if rising_edge(clk) then
            case state is
                when beg =>
                    rom_int <= 0;
                    ram_int <= 0;
                    iter_layer1 <= 0;
                    iter_layer2 <= 0;
                    max_idx <= 15;
                    max_weight <= X"8000";
                    mac_en <= '0';
                    ram_w <= '0';
                    if start='1' then
                        next_state <= romtoram0;
                    else
                        next_state <= beg;
                    end if;
                when romtoram0 =>
                    ram_w <= '1';
                    ram_din <= X"00" & rom_dout;
                    write_counter <= 0;
                    next_state <= ror_dummy;
                when ror_dummy =>
                    if write_counter = 3 then
                        ram_w <= '0';
                        if ram_int = 783 then
                            rom_int <= 1024;
                            ram_int <= 0;
                            next_state <= start_layer1;
                        else
                            rom_int <= rom_int + 1;
                            ram_int <= ram_int + 1;
                            next_state <= romtoram1;
                        end if;
                    else
                        write_counter <= write_counter + 1;
                        next_state <= ror_dummy;
                    end if;
                when romtoram1 =>
                    next_state <= romtoram0;
                when start_layer1 =>
                    iter_layer1 <= iter_layer1 + 1;
                    next_state <= mult_layer1;
                    mac_en <= '0';
                when mult_layer1 =>
                    if ram_int = 0 then
                        ctrl <= '1';
                    else
                        ctrl <= '0';
                    end if;
                    mac_en <= '1';
                    mac_din1 <= rom_dout;
                    mac_din2 <= ram_dout;
                    rom_int <= rom_int + 1;
                    ram_int <= ram_int + 1;
                    if ram_int = 783 then
                        next_state <= load_bias1;
                    else
                        next_state <= mult_inc1;
                    end if;
                when mult_inc1 =>
                    mac_en <= '0';
                    next_state <= mult_layer1;
                when load_bias1 =>
                    mac_en <= '0';
                    rom_int <= bias1 + iter_layer1;                   
                    next_state <= wait_bias1;
                when wait_bias1 =>
                    next_state <= add_layer1;
                when add_layer1 =>
                    if rom_dout(7)='1' then
                        sin <= std_logic_vector(signed(X"FF" & rom_dout) + signed(mac_dout));
                    else
                        sin <= std_logic_vector(signed(X"00" & rom_dout) + signed(mac_dout));
                    end if;
                    next_state <= relu_layer1;
                when relu_layer1 =>
                    cin <= sout;
                    next_state <= write_layer1;
                when write_layer1 =>
                    ram_int <= 783 + iter_layer1;
                    ram_w <= '1';
                    ram_din <= cout;
                    write_counter <= 0;
                    next_state <= dummy_layer1;
                when dummy_layer1 =>
                    if write_counter = 3 then
                        next_state <= back_layer1;
                        ram_w <= '0';
                    else
                        write_counter <= write_counter + 1;
                        next_state <= dummy_layer1;
                    end if;
                when back_layer1 =>
                    if iter_layer1 = 64 then
                        rom_int <= 51264;
                        ram_int <= 784;
                        next_state <= start_layer2;
                    else
                        rom_int <= 1024 + 784*iter_layer1;
                        ram_int <= 0;
                        next_state <= start_layer1;
                    end if;
                when start_layer2 =>
                    mac_en <= '0';
                    iter_layer2 <= iter_layer2 + 1;
                    next_state <= mult_layer2;
                when mult_layer2 =>
                    if ram_int = 784 then
                        ctrl <= '1';
                    else
                        ctrl <= '0';
                    end if;
                    mac_en <= '1';
                    mac_din1 <= rom_dout;
                    mac_din2 <= ram_dout;
                    rom_int <= rom_int + 1;
                    ram_int <= ram_int + 1;
                    if ram_int = 847 then
                        next_state <= load_bias2;
                    else
                        next_state <= mult_inc2;
                    end if;
                when mult_inc2 =>
                    mac_en <= '0';
                    next_state <= mult_layer2;
                when load_bias2 =>
                    mac_en <= '0';
                    rom_int <= bias2 + iter_layer2;
                    next_state <= wait_bias2;
                when wait_bias2 =>
                    next_state <= add_layer2;
                when add_layer2 =>
                    if rom_dout(7)='1' then
                        sin <= std_logic_vector(signed(X"FF" & rom_dout) + signed(mac_dout));
                    else
                        sin <= std_logic_vector(signed(X"00" & rom_dout) + signed(mac_dout));
                    end if;
                    next_state <= write_layer2;
                when write_layer2 =>
                    ram_int <= 847 + iter_layer2;
                    ram_w <= '1';
                    ram_din <= sout;
                    write_counter <= 0;
                    next_state <= dummy_layer2;
                when dummy_layer2 =>
                    if write_counter = 3 then
                        next_state <= back_layer2;
                        ram_w <= '0';
                    else
                        write_counter <= write_counter + 1;
                        next_state <= dummy_layer2;
                    end if;
                when back_layer2 =>
                    if iter_layer2 = 10 then
                        next_state <= ready_for_max;
                    else
                        rom_int <= 51264 + 64*iter_layer2;
                        ram_int <= 784;
                        next_state <= start_layer2;
                    end if;
                when ready_for_max =>
                    ram_int <= 848;
                    next_state <= wait_max;
                when wait_max =>
                    next_state <= iter_max;
                when iter_max =>
                    if signed(ram_dout) > signed(max_weight) then
                        gt <= '1';
                    else
                        gt <= '0';
                    end if;
                    next_state <= set_max;
                when set_max =>
                    if gt = '1' then
                        max_idx <= ram_int - 848;
                        max_weight <= ram_dout;
                    end if;
                    next_state <= inc_max;
                when inc_max =>
                    if ram_int = 857 then
                        next_state <= done;
                    else
                        ram_int <= ram_int + 1;
                        next_state <= wait_max;
                    end if;
                when done =>
                    inp <= std_logic_vector(to_unsigned(max_idx,4));
                    next_state <= done;
                when others => null; 
            end case;
        end if;
    end process;
end beh;