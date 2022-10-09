library IEEE;
use IEEE.std_logic_1164.all;


entity counter is 
	generic (
		count_width : integer);
	port(
		clk : in std_logic;
        clk_div : out std_logic);
end counter;

architecture beh of counter is
	signal count : integer:=0;
    signal tclk : std_logic := '1';
begin
	clk_div <= tclk;
	countProc : process(clk)
    begin
    	if rising_edge(clk) then
    	   if count+1=count_width then
    	       count <= 0;
    	       tclk <= not tclk;
    	   else
    	       count <= count + 1;
    	   end if;
        end if;
    end process countProc;
end beh;
