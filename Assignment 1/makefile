all:
	echo "Invalid command"

seven_seg:
	ghdl -a seven_seg.vhd
	ghdl -a seven_seg_tb.vhd
	ghdl -e seven_seg_tb
	ghdl -r seven_seg_tb --wave=seven_seg.ghw
	gtkwave seven_seg.ghw

combine:
	clear
	ghdl -a counterg.vhd
	ghdl -a counter7.vhd
	ghdl -a combine.vhd
	ghdl -a combine_tb.vhd
	ghdl -e combine_tb
	ghdl -r combine_tb --wave=combine.ghw --stop-time=100000ms
	gtkwave combine.ghw