library IEEE;
use IEEE.std_logic_1164.all;


entity counter7 is 
	generic (
		count_width : integer := 5000000);
	port(
		CLK : in std_logic;
        clk_OUT : out std_logic);
end counter7;

architecture counterArc of counter7 is
	signal count : integer:=0;
    signal tclk : std_logic := '1';
begin
	clk_OUT <= tclk;
	countProc : process(clk)
    begin
    	if rising_edge(clk) then
    	   if count+1=count_width then
    	       count <= 0;
    	       tclk <= not tclk;
		--    elsif count+1=count_width/2 then
		-- 		tclk <= not tclk;
    	   else
    	       count <= count + 1;
    	   end if;
        end if;
    end process countProc;
end counterArc;
