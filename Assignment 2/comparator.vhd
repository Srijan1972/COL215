library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity comparator is
    port(
        cin:in std_logic_vector(15 downto 0);
        cout:out std_logic_vector(15 downto 0));
end comparator;

architecture beh of comparator is
begin
    process(cin)
    begin
        if cin(15) = '0' then
            cout <= cin;
        else
            cout <= X"0000";
        end if;
    end process;
end architecture;