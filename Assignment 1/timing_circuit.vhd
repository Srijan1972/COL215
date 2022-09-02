library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;


entity timing_circuit is 
	port(clk : in std_logic;
   	muxsel : out std_logic_vector(1 downto 0);
        anodeOut : out std_logic_vector(3 downto 0));
end timing_circuit;

architecture timerarc of timing_circuit is
component counter7 is 
	generic(
		count_width : integer := 50000);
	port(
		CLK : in std_logic;
		run : in std_logic;
		rst : in std_logic;
        clk_OUT : out std_logic);
end component;
	signal count : integer:=0;
    signal ancount : std_logic_vector(3 downto 0) := "1110";
	signal run_control : std_logic:='1';
	signal rst_control : std_logic:='0';
	signal clk_div : std_logic;
begin
	divider:counter7 port map(clk,run_control,rst_control,clk_div);
	anodeOut <= ancount;
	muxsel <= std_logic_vector(to_unsigned(count,2));
	countProc : process(clk_div)
    begin
    	if rising_edge(clk_div) then
    	   	if (count = 3) then
    	   		count <= 0;
    	   		ancount <= "1110";
    	   	else
    	   		count <= count + 1;
    	   		ancount <= ancount(2 downto 0) & ancount(3);

    	   	end if;
        end if;
    end process countProc;
end timerarc;
