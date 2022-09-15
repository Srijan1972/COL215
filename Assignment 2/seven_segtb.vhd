--library ieee;
--use ieee.std_logic_1164.all;

--entity seven_seg_tb is
--end seven_seg_tb;

--architecture sim of seven_seg_tb is
--component seven_seg is
--    port(
--        inp  :in std_logic_vector(3 downto 0);
--        disp :out std_logic_vector(6 downto 0));
--end component;
--    signal inp:std_logic_vector(3 downto 0);
--    signal disp:std_logic_vector(6 downto 0);
--    signal expect:std_logic_vector(6 downto 0);

--begin
--    seven_seg_test:seven_seg port map(inp,disp);
--    process
--    begin
--        inp <= "0000"; expect <= "0001000";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 0" severity error;

--        inp <= "0001"; expect <= "1011011";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 1" severity error;

--        inp <= "0010"; expect <= "0100010";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 2" severity error;

--        inp <= "0011"; expect <= "0010010";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 3" severity error;

--        inp <= "0100"; expect <= "1010001";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 4" severity error;

--        inp <= "0101"; expect <= "0010100";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 5" severity error;

--        inp <= "0110"; expect <= "0000100";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 6" severity error;

--        inp <= "0111"; expect <= "1011010";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 7" severity error;

--        inp <= "1000"; expect <= "0000000";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 8" severity error;

--        inp <= "1001"; expect <= "0010000";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case 9" severity error;

--        inp <= "1010"; expect <= "1000000";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case A" severity error;

--        inp <= "1011"; expect <= "0000101";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case B" severity error;

--        inp <= "1100"; expect <= "0101100";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case C" severity error;

--        inp <= "1101"; expect <= "0000011";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case D" severity error;

--        inp <= "1110"; expect <= "0100100";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case E" severity error;

--        inp <= "1111"; expect <= "1100100";
--        wait for 1 ns;
--        assert expect=disp report "Failed at case F" severity error;

--        assert false report "Test complete" severity error;
--        wait;
--    end process;
--end architecture;

library ieee;
use ieee.std_logic_1164.all;

entity tb_seven_seg is
end tb_seven_seg;

architecture tb of tb_seven_seg is

    component seven_seg
        port (inp  : in std_logic_vector (3 downto 0);
              disp : out std_logic_vector (6 downto 0);
              an   : out std_logic_vector (3 downto 0));
    end component;

    signal inp  : std_logic_vector (3 downto 0);
    signal disp : std_logic_vector (6 downto 0);
    signal an   : std_logic_vector (3 downto 0);
    signal expect:std_logic_vector(6 downto 0);

begin

    dut : seven_seg
    port map (inp  => inp,
              disp => disp,
              an   => an);

    stimuli : process
    begin
        -- EDIT Adapt initialization as needed

        inp <= "0000"; expect <= "0001000";
        wait for 1 ns;
        assert expect=disp report "Failed at case 0" severity error;

        inp <= "0001"; expect <= "1011011";
        wait for 1 ns;
        assert expect=disp report "Failed at case 1" severity error;

        inp <= "0010"; expect <= "0100010";
        wait for 1 ns;
        assert expect=disp report "Failed at case 2" severity error;

        inp <= "0011"; expect <= "0010010";
        wait for 1 ns;
        assert expect=disp report "Failed at case 3" severity error;

        inp <= "0100"; expect <= "1010001";
        wait for 1 ns;
        assert expect=disp report "Failed at case 4" severity error;

        inp <= "0101"; expect <= "0010100";
        wait for 1 ns;
        assert expect=disp report "Failed at case 5" severity error;

        inp <= "0110"; expect <= "0000100";
        wait for 1 ns;
        assert expect=disp report "Failed at case 6" severity error;

        inp <= "0111"; expect <= "1011010";
        wait for 1 ns;
        assert expect=disp report "Failed at case 7" severity error;

        inp <= "1000"; expect <= "0000000";
        wait for 1 ns;
        assert expect=disp report "Failed at case 8" severity error;

        inp <= "1001"; expect <= "0010000";
        wait for 1 ns;
        assert expect=disp report "Failed at case 9" severity error;

        inp <= "1010"; expect <= "1000000";
        wait for 1 ns;
        assert expect=disp report "Failed at case A" severity error;

        inp <= "1011"; expect <= "0000101";
        wait for 1 ns;
        assert expect=disp report "Failed at case B" severity error;

        inp <= "1100"; expect <= "0101100";
        wait for 1 ns;
        assert expect=disp report "Failed at case C" severity error;

        inp <= "1101"; expect <= "0000011";
        wait for 1 ns;
        assert expect=disp report "Failed at case D" severity error;

        inp <= "1110"; expect <= "0100100";
        wait for 1 ns;
        assert expect=disp report "Failed at case E" severity error;

        inp <= "1111"; expect <= "1100100";
        wait for 1 ns;
        assert expect=disp report "Failed at case F" severity error;

        assert false report "Test complete" severity error;
        -- EDIT Add stimuli here

        wait;
    end process;

end tb;

-- Configuration block below is required by some simulators. Usually no need to edit.

--configuration cfg_tb_seven_seg of tb_seven_seg is
--    for tb
--    end for;
--end cfg_tb_seven_seg;