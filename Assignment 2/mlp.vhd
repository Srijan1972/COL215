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

component mac is
    port (
        ctrl:in std_logic;
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
    signal cin:std_logic_vector(15 downto 0);
    signal cout:std_logic_vector(15 downto 0);
    signal ctrl:std_logic;
    signal mac_din1:std_logic_vector(7 downto 0);
    signal mac_din2:std_logic_vector(15 downto 0);
    signal mac_dout:std_logic_vector(15 downto 0);
    signal ram_w:std_logic;
    signal ram_din:std_logic_vector(15 downto 0);
    signal ram_addr:std_logic_vector(9 downto 0);
    signal ram_dout:std_logic_vector(15 downto 0);
    signal rom_addr:std_logic_vector(15 downto 0);
    signal rom_dout:std_logic_vector(7 downto 0);
    signal inp:std_logic_vector(3 downto 0):=X"F";
    signal sin:std_logic_vector(15 downto 0);
    signal sout:std_logic_vector(15 downto 0);
    signal ready:std_logic:='0';
    signal ram_int:integer:=0;
    signal rom_int:integer:=0;
    signal iter_layer1:integer:=0;
    signal iter_layer2:integer:=0;
    signal bias1:integer:=51200;
    signal bias2:integer:=51904;
    type state_type is (beg,romtoram,start_layer1,mult_layer1,add_layer1,relu_layer1,write_layer1,back_layer1,start_layer2,mult_layer2,add_layer2,write_layer2,back_layer2,ready_for_max,find_max,done);
    signal state : state_type := beg;
    signal next_state : state_type := beg;
    signal max_idx:integer:=-1;
    signal max_weight:std_logic_vector(15 downto 0):=X"8000";
begin
    state <= next_state;
    ram_addr <= std_logic_vector(to_signed(ram_int,10));
    rom_addr <= std_logic_vector(to_signed(rom_int,16));
    relu:comparator port map(cin,cout);
    apple:mac port map(ctrl,mac_din1,mac_din2,mac_dout);
    local:ram port map(clk,ram_w,ram_din,ram_addr,ram_dout);
    global:rom generic map("imgdata_digit7.mif","weights_bias.mif") port map(rom_addr,rom_dout);
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
                    max_idx <= -1;
                    max_weight <= X"8000";
                    ram_w <= '0';
                    if start='1' then
                        next_state <= romtoram;
                    else
                        next_state <= beg;
                    end if;
                when romtoram =>
                    ram_w <= '1';
                    ram_din <= rom_dout;
                    rom_int <= rom_int + 1;
                    ram_int <= ram_int + 1;
                    if ram_int = 783 then
                        next_state <= start_layer1;
                    else
                        next_state <= romtoram;
                    end if;
                when start_layer1 =>
                    rom_int <= 1024 + 784*iter_layer1;
                    ram_int <= 0;
                    ram_w <= '0';
                    next_state <= mult_layer1;
                when mult_layer1 =>
                    if ram_int=0 then
                        ctrl <= '1';
                    else
                        ctrl <= '0';
                    end if;
                    mac_din1 <= rom_dout;
                    mac_din2 <= ram_dout;
                    rom_int <= rom_int + 1;
                    ram_int <= ram_int + 1;
                    if ram_int=783 then
                        next_state <= add_layer1;
                        rom_int <= bias1 + iter_layer1;
                    else
                        next_state <= mult_layer1;
                    end if;
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
                    ram_int <= 784 + iter_layer1;
                    ram_w <= '1';
                    ram_din <= cout;
                    next_state <= back_layer1;
                when back_layer1 =>
                    ram_w <= '0';
                    iter_layer1 <= iter_layer1 + 1;
                    if iter_layer1 = 63 then
                        next_state <= start_layer2;
                    else
                        next_state <= start_layer1;
                    end if;
                when start_layer2 => 
                    rom_int <= 51264 + 64*iter_layer2;
                    ram_int <= 784;
                    ram_w <= '0';
                    next_state <= mult_layer2;
                when mult_layer2 =>
                    if ram_int=784 then
                        ctrl <= '1';
                    else
                        ctrl <= '0';
                    end if;
                    mac_din1 <= rom_dout;
                    mac_din2 <= ram_dout;
                    rom_int <= rom_int + 1;
                    ram_int <= ram_int + 1;
                    if ram_int=847 then
                        next_state <= add_layer2;
                        rom_int <= bias2 + iter_layer2;
                    else
                        next_state <= mult_layer2;
                    end if;
                when add_layer2 =>
                    if rom_dout(7)='1' then
                        sin <= std_logic_vector(signed(X"FF" & rom_dout) + signed(mac_dout));
                    else
                        sin <= std_logic_vector(signed(X"00" & rom_dout) + signed(mac_dout));
                    end if;
                    next_state <= write_layer2;
                when write_layer2 =>
                    ram_int <= 848 + iter_layer2;
                    ram_w <= '1';
                    ram_din <= sin;
                    next_state <= back_layer2;
                when back_layer2 =>
                    ram_w <= '0';
                    iter_layer2 <= iter_layer2 + 1;
                    if iter_layer2 = 9 then
                        next_state <= ready_for_max;
                    else
                        next_state <= start_layer2;
                    end if;
                when ready_for_max =>
                    ram_int <= 848;
                    next_state <= find_max;
                when find_max =>
                    if to_integer(signed(ram_dout))>to_integer(signed(max_weight)) then
                        max_idx <= ram_int - 848;
                        max_weight <= ram_dout;
                    end if;
                    ram_int <= ram_int + 1;
                    if ram_int <= 857 then
                        next_state <= done;
                    else
                        next_state <= find_max;
                    end if;
                when done =>
                    inp <= std_logic_vector(to_signed(max_idx,4));
                    next_state <= done;
                when others => null; 
            end case;
        end if;
    end process;
end beh;