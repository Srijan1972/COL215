library ieee;
use ieee.std_logic_1164.all;

entity tb_mlp is
end tb_mlp;

architecture tb of tb_mlp is

    component mlp
        port (clk   : in std_logic;
              start : in std_logic;
              disp  : out std_logic_vector (6 downto 0);
              an    : out std_logic_vector (3 downto 0));
    end component;

    signal clk   : std_logic;
    signal start : std_logic;
    signal disp  : std_logic_vector (6 downto 0);
    signal an    : std_logic_vector (3 downto 0);

    constant TbPeriod : time := 10 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : mlp
    port map (clk   => clk,
              start => start,
              disp  => disp,
              an    => an);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk is really your main clock signal
    clk <= TbClock;

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        start <= '0';

        wait for 10 ns;
        start <= '1';

        wait for 110000 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_mlp of tb_mlp is
    for tb
    end for;
end cfg_tb_mlp;