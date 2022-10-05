library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity mac is
    port (
        ctrl:in std_logic;
        en:in std_logic;
        din1 :in std_logic_vector(7 downto 0); -- to be read from ROM
        din2 :in std_logic_vector(15 downto 0); -- to be read from RAM
        dout :out std_logic_vector(15 downto 0));
end mac;

architecture beh of mac is
    signal temp_reg:std_logic_vector(23 downto 0):=(others => '0');
begin
    dout <= temp_reg(15 downto 0);
    process(ctrl,din1,din2)
    begin
        if en='1' or en='0' then
            if ctrl='1' then
                temp_reg <= std_logic_vector(signed(din1) * signed(din2));
            else
                temp_reg <= std_logic_vector(signed(temp_reg) + signed(din1) * signed(din2));
            end if;
        end if;
    end process;
end beh;