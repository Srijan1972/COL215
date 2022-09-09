library IEEE;
use IEEE.std_logic_1164.all;
use ieee.numeric_std.all;
use IEEE.std_logic_unsigned.all;


entity debouncer is 
	generic ( count_width : integer);
	port(CLK : in std_logic;
    	button : in std_logic;
        stable : out std_logic);
end debouncer;

architecture debArc of debouncer is
	signal count : integer:=0;
    signal temp : std_logic := '0';
begin
	stable <= temp;
    countProc: process(CLK,button)
    begin
    	if(rising_edge(CLK)) then
            if(button = '1') then
                count <= count + 1;
                if(count = count_width -1) then
                    count <= 0;
                    temp <= '1';
                end if;
           else 
                count <= 0;
                temp <= '0';
           end if;
        end if;
    end process countProc;
end debArc;
