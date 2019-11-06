module DecimalCounter(clk,rst,CNT10);

input clk;
input rst;
output [3:0] CNT10;

wire  w3;
wire  w2;
wire  w10;
wire  w11;
wire  w12;
wire  w13;
wire  w14;
wire  w16;
wire  w17;
wire  w18;
wire  w19;
wire  w20;
wire  w21;
wire  w27;
wire  w28;
wire  w26;
wire  w29;
wire [3:0] b25;
wire  b25_3;
wire  b25_3_w24;
wire  b25_2;
wire  b25_2_w23;
wire  b25_1;
wire  b25_1_w22;
wire  b25_0;
wire  b25_0_w25;

assign w3 = clk;
assign w2 = rst;
assign CNT10 = b25;

assign b25[3] = b25_3;
assign b25[2] = b25_2;
assign b25[1] = b25_1;
assign b25[0] = b25_0;

assign b25_3_w24 = {b25[3]};
assign b25_2_w23 = {b25[2]};
assign b25_1_w22 = {b25[1]};
assign b25_0_w25 = {b25[0]};

PNU_DFF
     s0 (
      .clock(w3),
      .reset(w2),
      .Q(w29),
      .D(b25_0_w25));

PNU_DFF
     s1 (
      .clock(w3),
      .reset(w2),
      .Q(w28),
      .D(b25_1_w22));

PNU_DFF
     s2 (
      .clock(w3),
      .reset(w2),
      .Q(w27),
      .D(b25_2_w23));

PNU_DFF
     s3 (
      .clock(w3),
      .reset(w2),
      .Q(w26),
      .D(b25_3_w24));

PNU_AND2
     s4 (
      .i2(w10),
      .o1(w21),
      .i1(w26));

PNU_AND3
     s5 (
      .o1(w20),
      .i1(w27),
      .i2(w28),
      .i3(w29));

PNU_AND2
     s6 (
      .i2(w11),
      .o1(w19),
      .i1(w27));

PNU_AND2
     s7 (
      .i2(w12),
      .o1(w18),
      .i1(w27));

PNU_AND3
     s8 (
      .i1(w13),
      .o1(w17),
      .i2(w28),
      .i3(w29));

PNU_XOR2
     s9 (
      .o1(w16),
      .i1(w28),
      .i2(w29));

PNU_AND2
     s10 (
      .i2(w14),
      .i1(w16),
      .o1(b25_1));

PNU_NOT
     s11 (
      .i1(w29),
      .o1(b25_0));

PNU_NOT
     s12 (
      .o1(w14),
      .i1(w26));

PNU_NOT
     s13 (
      .o1(w13),
      .i1(w27));

PNU_NOT
     s14 (
      .o1(w12),
      .i1(w29));

PNU_NOT
     s15 (
      .o1(w11),
      .i1(w28));

PNU_NOT
     s16 (
      .o1(w10),
      .i1(w29));

PNU_OR2
     s17 (
      .i2(w20),
      .i1(w21),
      .o1(b25_3));

PNU_OR3
     s18 (
      .i3(w17),
      .i2(w18),
      .i1(w19),
      .o1(b25_2));

endmodule

