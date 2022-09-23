library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity mlp is
    port(
        clk:in std_logic;
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
    signal inp:std_logic_vector(3 downto 0):=X"C";
    signal sin:std_logic_vector(15 downto 0);
    signal sout:std_logic_vector(15 downto 0);
    signal ready:std_logic:='0';
    signal ram_int:integer:=0;
    signal rom_int:integer:=0;
begin
    ram_addr <= std_logic_vector(to_signed(ram_int,10));
    rom_addr <= std_logic_vector(to_signed(rom_int,16));
    relu:comparator port map(cin,cout);
    apple:mac port map(ctrl,mac_din1,mac_din2,mac_dout);
    local:ram port map(clk,ram_w,ram_din,ram_addr,ram_dout);
    global:rom generic map("imgdata_digit7.mif","weights_bias.mif") port map(rom_addr,rom_dout);
    div:shifter port map(sin,sout);
    display:seven_seg port map(inp,disp,an);
end beh;