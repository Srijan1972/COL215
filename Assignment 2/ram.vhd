library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ram is
    port (
        clk :in std_logic;
        re  :in std_logic;
        we  :in std_logic;
        din :in std_logic_vector(7 downto 0);
        addr:in std_logic_vector(16 downto 0);
        dout:out std_logic_vector(7 downto 0));
end entity;

architecture beh of ram is
    type mem_array is array (0 to 131071) of std_logic_vector(7 downto 0);
    signal ra_mem:mem_array:=(others => X"00");
begin
    process(clk,re)
    begin
        if rising_edge(clk) and re='1' then
            dout <= ra_mem(to_integer(unsigned(addr)));
        end if;
    end process;
    process(clk,we)
    begin
        if rising_edge(clk) and we='1' then
            ra_mem(to_integer(unsigned(addr))) <= din;
        end if;
    end process;
end beh;