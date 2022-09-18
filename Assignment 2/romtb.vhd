library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_rom is
end tb_rom;

architecture tb of tb_rom is
    component rom
      generic(
          img_file:string:="imgdata_digit7.mif";
          params_file:string:="weights_bias.mif");
        port (addr : in std_logic_vector (15 downto 0);
              dout : out std_logic_vector (7 downto 0));
    end component;

    signal addr : std_logic_vector (15 downto 0);
    signal dout : std_logic_vector (7 downto 0);
    signal temp : integer := 0;
begin
    addr <= std_logic_vector(to_unsigned(temp,16));
    dut : rom
    port map (addr => addr,
              dout => dout);

    stimuli : process
    begin
        temp <= temp + 1;
        wait for 1 ns;
        if temp = 65535 then
            wait;
        end if;
    end process;

end tb;