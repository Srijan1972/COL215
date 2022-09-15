library ieee;
use ieee.std_logic_1164.all;

entity tb_comparator is
end tb_comparator;

architecture tb of tb_comparator is

    component comparator
        port (cin  : in std_logic_vector (15 downto 0);
              cout : out std_logic_vector (15 downto 0));
    end component;

    signal cin  : std_logic_vector (15 downto 0);
    signal cout : std_logic_vector (15 downto 0);

begin

    dut : comparator
    port map (cin  => cin,
              cout => cout);

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        cin <= (others => '0');

        -- EDIT Add stimuli here

        wait;
    end process;

end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

--configuration cfg_tb_comparator of tb_comparator is
--    for tb
--    end for;
--end cfg_tb_comparator;