library ieee;
use ieee.std_logic_1164.all;

entity tb_shifter is
end tb_shifter;

architecture tb of tb_shifter is

    component shifter
        port (sin  : in std_logic_vector (15 downto 0);
              sout : out std_logic_vector (15 downto 0));
    end component;

    signal sin  : std_logic_vector (15 downto 0);
    signal sout : std_logic_vector (15 downto 0);

    constant TbPeriod : time := 100 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : shifter
    port map (sin  => sin,
              sout => sout);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk is really your main clock signal

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        sin <= (others => '0');
        wait for 100 ns;
        sin <= x"001f";
        wait for 100 ns;
        sin <= x"0ff0";
        wait for 100 ns;
        sin <= x"0110";
        -- EDIT Add stimuli here
        wait for 5 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

end tb;
