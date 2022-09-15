library ieee;
use ieee.std_logic_1164.all;

entity tb_mac is
end tb_mac;

architecture tb of tb_mac is

    component mac
        port (clk  : in std_logic;
              ctrl : in std_logic;
              din1 : in std_logic_vector (7 downto 0);
              din2 : in std_logic_vector (15 downto 0);
              dout : out std_logic_vector (15 downto 0));
    end component;

    signal clk  : std_logic;
    signal ctrl : std_logic;
    signal din1 : std_logic_vector (7 downto 0);
    signal din2 : std_logic_vector (15 downto 0);
    signal dout : std_logic_vector (15 downto 0);

    constant TbPeriod : time := 100 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : mac
    port map (clk  => clk,
              ctrl => ctrl,
              din1 => din1,
              din2 => din2,
              dout => dout);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk is really your main clock signal
    clk <= TbClock;

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        ctrl <= '0';
        din1 <= (others => '0');
        din2 <= (others => '0');
        wait for 100 ns;
        din1 <= x"05";
        din2 <= x"0005";
        wait for 100 ns;
        din1 <= x"15";
        din2 <= x"0105";
        wait for 100 ns;
        ctrl <= '1';
        din1 <= x"05";
        din2 <= x"0005";
        wait for 100 ns;
        din1 <= x"15";
        din2 <= x"0105";
        wait for 100 ns;
        din1 <= x"f5";
        din2 <= x"f0f5";
        wait for 100 ns;
        ctrl <= '0';
        din1 <= x"05";
        din2 <= x"0005";
        wait for 100 ns;

        -- EDIT Add stimuli here
        wait for 5 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

configuration cfg_tb_mac of tb_mac is
    for tb
    end for;
end cfg_tb_mac;