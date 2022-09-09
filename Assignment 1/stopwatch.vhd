library ieee;
use ieee.std_logic_1164.all;

entity stopwatch is
    port(
        clk : in std_logic;
        start : in std_logic;
        pause : in std_logic;
        reset : in std_logic;
        display : out std_logic_vector(6 downto 0);
        an : out std_logic_vector(3 downto 0);
        dp : out std_logic);
end stopwatch;

architecture beh of stopwatch is
component combine is
    port(
        clk :in std_logic;
        run :in std_logic;
        rst :in std_logic;
        tenth_seconds:out std_logic_vector(3 downto 0);
        seconds:out std_logic_vector(3 downto 0);
        ten_seconds:out std_logic_vector(3 downto 0);
        minutes:out std_logic_vector(3 downto 0));
end component;

component mux is
    port(
        inp0 : in std_logic_vector(3 downto 0);
        inp1 : in std_logic_vector(3 downto 0);
        inp2 : in std_logic_vector(3 downto 0);
        inp3 : in std_logic_vector(3 downto 0);
        sel  : in std_logic_vector(1 downto 0);
        dp   : out std_logic;
        outp : out std_logic_vector(3 downto 0));
end component;

component seven_seg is
    port(
        inp  :in std_logic_vector(3 downto 0);
        disp :out std_logic_vector(6 downto 0)
    );
end component;

component timing_circuit is 
	port(clk : in std_logic;
   	muxsel : out std_logic_vector(1 downto 0);
        anodeOut : out std_logic_vector(3 downto 0));
end component;

component debouncer is 
	generic ( count_width : integer:=1000000);
	port(CLK : in std_logic;
    	button : in std_logic;
        stable : out std_logic);
end component;
    signal sel:std_logic_vector(1 downto 0);
    signal sev_inp:std_logic_vector(3 downto 0);
    signal enable_watch:std_logic:='0';
    signal tenth_seconds:std_logic_vector(3 downto 0);
    signal seconds:std_logic_vector(3 downto 0);
    signal ten_seconds:std_logic_vector(3 downto 0);
    signal minutes:std_logic_vector(3 downto 0);
    signal reset_watch:std_logic;
    signal start_debounced:std_logic;
    signal pause_debounced:std_logic;
begin
    combined: combine port map(clk,enable_watch,reset_watch,tenth_seconds,seconds,ten_seconds,minutes);
    timcirc: timing_circuit port map(clk,sel,an);
    plex : mux port map(tenth_seconds,seconds,ten_seconds,minutes,sel,dp,sev_inp); 
    seg_disp: seven_seg port map(sev_inp,display);
    rst_debounce: debouncer port map(clk,reset,reset_watch);
    st_debounce: debouncer port map(clk,start,start_debounced);
    ps_debounce: debouncer port map(clk,pause,pause_debounced);
    process(start_debounced,pause_debounced)
    begin
        if start_debounced='1' then
            enable_watch <= '1';
        elsif pause_debounced='1' then
            enable_watch <= '0';
        end if;
    end process;
end beh;