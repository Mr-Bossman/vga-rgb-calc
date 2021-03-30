a way to make vga signals from rgb this is a dac that goes from 0 -> .7 and it will calculate the resistors for you based on how many bits u have 
based of of https://olimex.wordpress.com/2012/06/12/low-cost-lcd-to-vga-adapter/


example code for vga in the linux kernel 

static const struct drm_display_mode vga_mode = {
	.clock = 25175,
	.hdisplay = 640,
	.hsync_start = 640 + 16,
	.hsync_end = 640 + 16 + 96,
	.htotal = 640 + 16 + 96 + 48,
	.vdisplay = 480,
	.vsync_start = 480 + 10,
	.vsync_end = 640 + 10 + 2,
	.vtotal = 480 + 10 + 2 + 33,
	.vrefresh = 60,
};
static const struct panel_desc vga = {
	.modes = &vga_mode,
	.num_modes = 1,
	.bpc = 16,
	.size = {
		.width = 151,
		.height = 91,
	},
	.bus_format = MEDIA_BUS_FMT_RGB888_1X7X4_SPWG,
};