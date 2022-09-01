library ieee;
use ieee.std_logic_1164.all;

entity mux is
    port(
        inp1 : in std_logic_vector(3 downto 0);
        inp2 : in std_logic_vector(3 downto 0);
        inp3 : in std_logic_vector(3 downto 0);
        inp4 : in std_logic_vector(3 downto 0);
        sel  : in std_logic_vector(1 downto 0);
        outp : out std_logic_vector(3 downto 0));
end mux;

architecture beh of mux is
begin
    process(inp1,inp2,inp3,inp4,sel)
    begin
        case sel is
            when "00" => outp <= inp1;
            when "01" => outp <= inp2;
            when "10" => outp <= inp3;
            when others => outp <= inp4;
        end case;
    end process;
end beh;