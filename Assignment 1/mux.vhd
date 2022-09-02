library ieee;
use ieee.std_logic_1164.all;

entity mux is
    port(
        inp0 : in std_logic_vector(3 downto 0);
        inp1 : in std_logic_vector(3 downto 0);
        inp2 : in std_logic_vector(3 downto 0);
        inp3 : in std_logic_vector(3 downto 0);
        sel  : in std_logic_vector(1 downto 0);
        dp   : out std_logic;
        outp : out std_logic_vector(3 downto 0));
end mux;

architecture beh of mux is
begin
    process(inp0,inp1,inp2,inp3,sel)
    begin
        case sel is
            when "00" => outp <= inp0; dp <= '1';
            when "01" => outp <= inp1; dp <= '0';
            when "10" => outp <= inp2; dp <= '1';
            when "11" => outp <= inp3; dp <= '0';
            when others => outp <= "XXXX"; dp <= 'X';
        end case;
    end process;
end beh;