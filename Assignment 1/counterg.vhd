library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;

entity counter is 
	generic ( count_width : integer);
	port(CLK : in std_logic;
		run : in std_logic;
		rst : in std_logic;
   	count_OUT : out std_logic_vector(3 downto 0);
        clk_OUT : out std_logic);
end counter;

architecture counterArc of counter is

	signal count : integer:=0;
    signal tclk : std_logic := '1';
begin
	clk_OUT <= tclk;
	count_out <= std_logic_vector(to_unsigned(count,4));
	countProc : process(clk,run,rst)
    begin
		if rst = '1' then
			count <= 0;
			tclk <= '1';
    	elsif rising_edge(clk) and run = '1' then
    	   if count+1=count_width then
    	       count <= 0;
    	       tclk <= not tclk;
           elsif count+1=count_width/2 then
    	       tclk <= not tclk;
               count <= count + 1;
    	   else
    	       count <= count + 1;
    	   end if;
        end if;
    end process countProc;
end counterArc;
