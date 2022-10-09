library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;

entity rom is
    generic(
        img_file:string;
        params_file:string);
    port(
        clk :in std_logic;
        addr:in std_logic_vector(15 downto 0);
        dout:out std_logic_vector(7 downto 0));
end entity;

architecture beh of rom is
    type mem_array is array (0 to 65535) of std_logic_vector(7 downto 0);

    impure function load_img(img:in string) return mem_array is
        file mif_file : text open read_mode is img;
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

    impure function load_params (params:in string;mem:in mem_array) return mem_array is
        file mif_file : text open read_mode is params;
        variable mif_line : line;
        variable temp_bv : bit_vector(7 downto 0);
        variable temp_mem : mem_array:=mem;
    begin
        for i in 0 to 50889 loop
            readline(mif_file, mif_line);
            read(mif_line, temp_bv);
            temp_mem(1024+i) := to_stdlogicvector(temp_bv);
        end loop;
        return temp_mem;
    end function;
    signal ro_mem:mem_array:=load_params(params_file,load_img(img_file));
begin
    process(clk)
    begin
        if rising_edge(clk) then
            dout <= ro_mem(to_integer(unsigned(addr)));
        end if;
    end process;
end beh;
