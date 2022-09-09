library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity registers is
    port (
        clk :in std_logic;
        re  :in std_logic;
        we  :in std_logic;
        addr:in std_logic_vector(3 downto 0);
        din :in std_logic_vector(7 downto 0);
        dout:out std_logic(7 downto 0));
end registers;

architecture beh of registers is
    type regs is array (0 to 15) of std_logic_vector(7 downto 0);
    signal register_file:regs:=(others => X"00");
begin
    process(clk,re)
    begin
        if rising_edge(clk) and re='1' then
            dout <= register_file(to_integer(unsigned(addr)));
        end if;
    end process;
    process(clk,we)
    begin
        if rising_edge(clk) and we='1' then
            register_file(to_integer(unsigned(addr))) <= din;
        end if;
    end process;
end beh;