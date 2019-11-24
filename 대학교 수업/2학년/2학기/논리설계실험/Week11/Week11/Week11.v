module Week11(rst,clk,star,pound,num4,num5,num6,num7,num8,num9,num0,num1,num2,num3,Out);

input rst;
input clk;
input star;
input pound;
input num4;
input num5;
input num6;
input num7;
input num8;
input num9;
input num0;
input num1;
input num2;
input num3;
output Out;

wire  w8;
wire  w10;
wire  w11;
wire [1:0] b11;
wire [1:0] b33;
wire  w17;
wire  w16;
wire  w15;
wire  w19;
wire [1:0] b17;
wire  w21;
wire [3:0] b19;
wire [1:0] b20;
wire [1:0] b21;
wire  w27;
wire  w28;
wire  w29;
wire  w30;
wire  w31;
wire  w32;
wire  w33;
wire  w34;
wire  w35;
wire  w36;
wire  w38;
wire  w7;
wire  w39;
wire  w40;
wire  w41;
wire  w45;
wire  w55;
wire  w56;
wire  w9;
wire [3:0] b47;
wire  w52;
wire  w47;
wire  b33_0_w12;
wire  b11_0_w13;
wire  b20_0;
wire  b20_1;
wire  b17_1_w23;
wire  b21_1_w24;
wire  b21_0_w25;
wire  b17_0_w26;
wire  b33_0_w37;
wire  b47_2_w49;
wire  b47_1_w50;
wire  b47_0_w51;

assign w52 = rst;
assign w47 = clk;
assign w8 = star;
assign w11 = pound;
assign w31 = num4;
assign w32 = num5;
assign w33 = num6;
assign w34 = num7;
assign w35 = num8;
assign w36 = num9;
assign w27 = num0;
assign w28 = num1;
assign w29 = num2;
assign w30 = num3;
assign Out = w45;

assign b20[1] = b20_1;
assign b20[0] = b20_0;

assign b33_0_w12 = {b33[0]};
assign b11_0_w13 = {b11[0]};
assign b17_1_w23 = {b17[1]};
assign b21_1_w24 = {b21[1]};
assign b21_0_w25 = {b21[0]};
assign b17_0_w26 = {b17[0]};
assign b33_0_w37 = {b33[0]};
assign b47_2_w49 = {b47[2]};
assign b47_1_w50 = {b47[1]};
assign b47_0_w51 = {b47[0]};

SramFxF
     s0 (
      .RW(w21),
      .Din(b19),
      .ADRESS(b20),
      .DataOut(b47),
      .RST(w52));

DecimalToBinary
     s1 (
      .CHK(w19),
      .Dout(b19),
      .d0(w27),
      .d1(w28),
      .d2(w29),
      .d3(w30),
      .d4(w31),
      .d5(w32),
      .d6(w33),
      .d7(w34),
      .d8(w35),
      .d9(w36));

LTP
     s2 (
      .Pulse(w15),
      .Level(w19),
      .rst(w52),
      .clk(w47));

TwobitCounter
     s3 (
      .clk(w8),
      .rst(w10),
      .Cnt4(b11));

TwobitCounter
     s5 (
      .rst(w8),
      .clk(w11),
      .Cnt4(b33));

PNU_OR2
     s6 (
      .o1(w10),
      .i2(w11),
      .i1(w52));

PNU_MUX4
     s7 (
      .e2(b33_0_w12),
      .e1(b11_0_w13),
      .i2(w17),
      .i3(w16),
      .i4(w16),
      .i1(w16),
      .o1(w21));

PNU_ZERO
     s8 (
      .o1(w16));

PNU_ONE
     s9 (
      .o1(w17));

TwobitCounter
     s10 (
      .clk(w15),
      .Cnt4(b17),
      .rst(w52));

PNU_MUX2
     s12 (
      .o1(b20_1),
      .i1(b17_1_w23),
      .i2(b21_1_w24),
      .e1(b33_0_w37));

PNU_MUX2
     s13 (
      .o1(b20_0),
      .i2(b21_0_w25),
      .i1(b17_0_w26),
      .e1(b33_0_w37));

PNU_CLK_DIV
     #(
      .cnt_num(3822))
     s14 (
      .div_clk(w56),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(3405))
     s15 (
      .div_clk(w55),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(3033))
     s16 (
      .div_clk(w40),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(2683))
     s17 (
      .div_clk(w41),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(2551))
     s4 (
      .div_clk(w38),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(2272))
     s18 (
      .div_clk(w7),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(2024))
     s19 (
      .div_clk(w39),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_CLK_DIV
     #(
      .cnt_num(1911))
     s20 (
      .div_clk(w9),
      .rst(w52),
      .clk(w47),
      .en(w47));

PNU_MUX8
     s21 (
      .i5(w38),
      .i6(w7),
      .i7(w39),
      .i3(w40),
      .i4(w41),
      .o1(w45),
      .i2(w55),
      .i1(w56),
      .i8(w9),
      .e1(b47_2_w49),
      .e2(b47_1_w50),
      .e3(b47_0_w51));

TwobitCounter
     s22 (
      .clk(w19),
      .Cnt4(b21),
      .rst(w52));

endmodule

