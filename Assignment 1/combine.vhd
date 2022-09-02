library ieee;
use ieee.std_logic_1164.all;

entity combine is
    port(
        clk :in std_logic;
        run :in std_logic;
        rst :in std_logic;
        tenth_seconds:out std_logic_vector(3 downto 0);
        seconds:out std_logic_vector(3 downto 0);
        ten_seconds:out std_logic_vector(3 downto 0);
        minutes:out std_logic_vector(3 downto 0));
end combine;

architecture beh of combine is
component counter is 
	generic(
        count_width : integer);
	port(
        CLK : in std_logic;
        run : in std_logic;
		rst : in std_logic;
   	    count_OUT : out std_logic_vector(3 downto 0);
        clk_OUT : out std_logic);
end component;

component counter7 is 
	generic (
		count_width : integer := 5000000);
	port(
		CLK : in std_logic;
        run : in std_logic;
		rst : in std_logic;
        clk_OUT : out std_logic);
end component;
    signal drive1:std_logic;
    signal drive2:std_logic;
    signal drive3:std_logic;
    signal drive4:std_logic;
    signal drive5:std_logic;
begin
    freq_divider:counter7 port map(clk,run,rst,drive1);
    tenth_seconds_disp:counter generic map(10) port map(drive1,run,rst,tenth_seconds,drive2);
    seconds_disp:counter generic map(10) port map(drive2,run,rst,seconds,drive3);
    ten_seconds_disp:counter generic map(6) port map(drive3,run,rst,ten_seconds,drive4);
    minutes_disp:counter generic map(10) port map(drive4,run,rst,minutes,drive5);
end beh;