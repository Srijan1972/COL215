library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity combine_tb is
end entity;

architecture sim of combine_tb is
component combine is
        port(
        clk :in std_logic;
        tenth_seconds:out std_logic_vector(3 downto 0);
        seconds:out std_logic_vector(3 downto 0);
        ten_seconds:out std_logic_vector(3 downto 0);
        minutes:out std_logic_vector(3 downto 0));
end component;
    signal clk :std_logic:='1';
    signal tenth_seconds:std_logic_vector(3 downto 0);
    signal seconds:std_logic_vector(3 downto 0);
    signal ten_seconds:std_logic_vector(3 downto 0);
    signal minutes:std_logic_vector(3 downto 0);
begin
    combine_test:combine port map(clk,tenth_seconds,seconds,ten_seconds,minutes);
    process
    begin
        wait for 5 ms;
        clk <= not clk;
    end process;
end sim;