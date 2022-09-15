library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity shifter is
    port(
        sen:in std_logic;
        clk:in std_logic;
        sin:in std_logic_vector(15 downto 0);
        sout:out std_logic_vector(15 downto 0));
end entity shifter;

architecture beh of shifter is
begin
    process(sin,sen,clk)
    begin
        if(rising_edge(clk) and sen = '1') then
            if sin(15) = '1' then
                sout <= "11111" & sin(15 downto 5);
            else
                sout <= "00000" & sin(15 downto 5);
            end if;
        end if;
    end process;
end architecture;