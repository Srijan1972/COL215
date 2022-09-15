library ieee;
use ieee.std_logic_1164.all;

entity tb_ram is
end tb_ram;

architecture tb of tb_ram is

    component ram
        port (clk  : in std_logic;
              w    : in std_logic;
              din  : in std_logic_vector (15 downto 0);
              addr : in std_logic_vector (9 downto 0);
              dout : out std_logic_vector (15 downto 0));
    end component;

    signal clk  : std_logic;
    signal w    : std_logic;
    signal din  : std_logic_vector (15 downto 0);
    signal addr : std_logic_vector (9 downto 0);
    signal dout : std_logic_vector (15 downto 0);

    constant TbPeriod : time := 50 ns; -- EDIT Put right period here
    signal TbClock : std_logic := '0';
    signal TbSimEnded : std_logic := '0';

begin

    dut : ram
    port map (clk  => clk,
              w    => w,
              din  => din,
              addr => addr,
              dout => dout);

    -- Clock generation
    TbClock <= not TbClock after TbPeriod/2 when TbSimEnded /= '1' else '0';

    -- EDIT: Check that clk is really your main clock signal
    clk <= TbClock;

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed
        w <= '0';
        din <= (others => '0');
        addr <= (others => '0');
        wait for 100 ns;
        w <= '1';
        addr <= "0000000101";
        din <= x"1010";
        wait for 100 ns;
        addr <= "0000000001";
        din <= x"f010";
        w <= '0';
        wait for 100 ns;
        addr <= "0000000101";
        wait for 100 ns;
        addr <= "0000000001";

        wait for 100 * TbPeriod;

        -- Stop the clock and hence terminate the simulation
        TbSimEnded <= '1';
        wait;
    end process;

end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

--configuration cfg_tb_ram of tb_ram is
--    for tb
--    end for;
--end cfg_tb_ram;