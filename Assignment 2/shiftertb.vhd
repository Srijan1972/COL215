library ieee;
use ieee.std_logic_1164.all;

entity tb_shifter is
end tb_shifter;

architecture tb of tb_shifter is

    component shifter
        port (sen  : in std_logic;
              clk  : in std_logic;
              sin  : in std_logic_vector (15 downto 0);
              sout : out std_logic_vector (15 downto 0));
    end component;

    signal sen  : std_logic;
    signal clk  : std_logic;
    signal sin  : std_logic_vector (15 downto 0);
    signal sout : std_logic_vector (15 downto 0);

    constant TbPeriod : time := 100 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : shifter
    port map (sen  => sen,
              clk  => clk,
              sin  => sin,
              sout => sout);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk is really your main clock signal
    clk <= TbClock;

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        sen <= '0';
        sin <= (others => '0');
        wait for 100 ns;
        sen <= '1';
        sin <= x"001f";
        wait for 100 ns;
        sin <= x"0ff0";
        wait for 100 ns;
        sen <= '0';
        wait for 10 ns;
        sin <= x"0110";
        -- EDIT Add stimuli here
        wait for 5 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_shifter of tb_shifter is
    for tb
    end for;
end cfg_tb_shifter;