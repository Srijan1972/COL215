library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ram is
    port (
        clk :in std_logic;
        w   :in std_logic;
        din :in std_logic_vector(15 downto 0);
        addr:in std_logic_vector(9 downto 0);
        dout:out std_logic_vector(15 downto 0));
end entity;

architecture beh of ram is
    type mem_array is array (0 to 1023) of std_logic_vector(15 downto 0);
    signal ra_mem:mem_array:=(others => X"0000");
begin
    dout <= ra_mem(to_integer(unsigned(addr)));
    process(clk)
    begin
        if rising_edge(clk) and w='1' then
            ra_mem(to_integer(unsigned(addr))) <= din;
        end if;
    end process;
end beh;
