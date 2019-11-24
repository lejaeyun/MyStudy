module Piezo(clk,rst,num0,num3,num4,num5,num6,num7,num1,num2,Out);

input clk;
input rst;
input num0;
input num3;
input num4;
input num5;
input num6;
input num7;
input num1;
input num2;
output Out;

wire  w0;
wire  w3;
wire  w6;
wire  w7;
wire  w8;
wire  w12;
wire  w13;
wire  w15;
wire  w16;
wire  w17;
wire  w18;
wire  w19;
wire  w20;
wire  w21;
wire  w22;
wire  w23;
wire  w24;
wire  w25;
wire  w26;
wire  w27;
wire  w11;
wire  w10;
wire  w9;
wire  w28;

assign w0 = clk;
assign w3 = rst;
assign w26 = num0;
assign w23 = num3;
assign w22 = num4;
assign w21 = num5;
assign w20 = num6;
assign w19 = num7;
assign w25 = num1;
assign w24 = num2;
assign Out = w18;

PNU_CLK_DIV
     #(
      .cnt_num(3822))
     s0 (
      .clk(w0),
      .rst(w3),
      .div_clk(w10),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(3405))
     s1 (
      .clk(w0),
      .rst(w3),
      .div_clk(w11),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(3004))
     s2 (
      .clk(w0),
      .rst(w3),
      .div_clk(w12),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(2683))
     s3 (
      .clk(w0),
      .rst(w3),
      .div_clk(w13),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(2551))
     s4 (
      .clk(w0),
      .rst(w3),
      .div_clk(w6),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(2723))
     s5 (
      .clk(w0),
      .rst(w3),
      .div_clk(w7),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(2105))
     s6 (
      .clk(w0),
      .rst(w3),
      .div_clk(w8),
      .en(w28));

PNU_CLK_DIV
     #(
      .cnt_num(1911))
     s7 (
      .clk(w0),
      .rst(w3),
      .div_clk(w9),
      .en(w28));

PNU_MUX8
     s8 (
      .i5(w6),
      .i6(w7),
      .i7(w8),
      .i3(w12),
      .i4(w13),
      .e1(w15),
      .e3(w16),
      .e2(w17),
      .o1(w18),
      .i2(w11),
      .i1(w10),
      .i8(w9));

DecimalToBinaryWithCHK
     s10 (
      .b2(w15),
      .b0(w16),
      .b1(w17),
      .d7(w19),
      .d6(w20),
      .d5(w21),
      .d4(w22),
      .d3(w23),
      .d2(w24),
      .d1(w25),
      .d0(w26),
      .d8(w27),
      .d9(w27),
      .CHK(w28),
      .b3());

PNU_ZERO
     s12 (
      .o1(w27));

endmodule

