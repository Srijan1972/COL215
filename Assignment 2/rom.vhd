library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;

entity rom is
    generic(
        img_file:string:="sample.mif");
    port(
        clk :in std_logic;
        re  :in std_logic;
        addr:in std_logic_vector(16 downto 0);
        dout:out std_logic_vector(7 downto 0));
end entity;

architecture beh of rom is
    type mem_array is array (0 to 131071) of std_logic_vector(7 downto 0);

    impure function init_mem(mif_file_name:in string) return mem_array is
        file mif_file : text open read_mode is mif_file_name;
        variable mif_line : line;
        variable temp_bv : bit_vector(7 downto 0);
        variable temp_mem : mem_array;
    begin
        for i in 0 to 783 loop
            readline(mif_file, mif_line);
            read(mif_line, temp_bv);
            temp_mem(i) := to_stdlogicvector(temp_bv);
        end loop;
        return temp_mem;
    end function;
    signal ro_mem:mem_array:=init_mem(img_file);
begin
    process(clk,re)
    begin
        if rising_edge(clk) and re='1' then
            dout <= ro_mem(to_integer(unsigned(addr)));
        end if;
    end process;
end beh;