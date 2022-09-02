library ieee;
use ieee.std_logic_1164.all;

entity seven_seg is
    port(
        inp  :in std_logic_vector(3 downto 0);
        disp :out std_logic_vector(6 downto 0)
    );
end seven_seg;

architecture beh of seven_seg is
    signal disp_temp:std_logic_vector(6 downto 0);
begin
    disp <= disp_temp;
    -- -- 0 --
    -- |     |
    -- 1     2
    -- | -3- |
    -- 4     5
    -- |     |
    -- -- 6 --
    process(inp)
    begin
        disp_temp(0) <= ((not inp(3)) and inp(2) and (not inp(1)) and (not inp(0))) or ((not inp(3)) and (not inp(2)) and (not inp(1)) and inp(0)) or (inp(3) and inp(2) and (not inp(1)) and inp(0)) or (inp(3) and (not inp(2)) and inp(1) and inp(0));
        disp_temp(1) <= (inp(3) and inp(2) and (not inp(1)) and inp(0)) or ((not inp(3)) and inp(1) and inp(0)) or ((not inp(3)) and (not inp(2)) and inp(0)) or ((not inp(3)) and (not inp(2)) and inp(1));
        disp_temp(2) <= (inp(3) and inp(2) and (not inp(0))) or (inp(3) and inp(1) and inp(0)) or (inp(2) and inp(1) and (not inp(0))) or ((not inp(3)) and inp(2) and (not inp(1)) and inp(0));
        disp_temp(3) <= ((not inp(3)) and (not inp(2)) and (not inp(1))) or (inp(3) and inp(2) and (not inp(1)) and (not inp(0))) or ((not inp(3)) and inp(2) and inp(1) and inp(0));
        disp_temp(4) <= ((not inp(3)) and inp(0)) or ((not inp(3)) and inp(2) and (not inp(1))) or ((not inp(2)) and (not inp(1)) and inp(0));
        disp_temp(5) <= (inp(3) and inp(2) and inp(1)) or (inp(3) and inp(2) and (not inp(0))) or ((not inp(3)) and (not inp(2)) and inp(1) and (not inp(0)));
        disp_temp(6) <= ((not inp(3)) and (not inp(2)) and (not inp(1)) and inp(0)) or ((not inp(3)) and inp(2) and (not inp(1)) and (not inp(0))) or (inp(2) and inp(1) and inp(0)) or (inp(3) and (not inp(2)) and inp(1) and (not inp(0)));
    end process;
end beh;