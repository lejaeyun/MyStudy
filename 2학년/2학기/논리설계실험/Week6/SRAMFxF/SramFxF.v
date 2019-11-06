module SramFxF(RST,ADRESS,DataOut,Din,RW);

input RST;
input [1:0] ADRESS;
output [3:0] DataOut;
input [3:0] Din;
input RW;

wire  w0;
wire [1:0] b1;
wire [3:0] b30;
wire [3:0] b56;
wire [3:0] b57;
wire [3:0] b39;
wire  w51;
wire  w54;
wire  w57;
wire  w53;
wire  w59;
wire  w61;
wire  w60;
wire  w58;
wire  w62;
wire  w63;
wire [3:0] b55;
wire [3:0] b53;
wire  b39_0;
wire  b39_1;
wire  b39_2;
wire  b39_3;
wire  b1_0_w56;
wire  b1_1_w55;
wire  b1_1_w69;
wire  b1_0_w70;
wire  b1_1_w71;
wire  b1_0_w72;
wire  b57_2_w73;
wire  b56_2_w66;
wire  b55_2_w74;
wire  b1_0_w75;
wire  b1_1_w76;
wire  b57_1_w77;
wire  b56_1_w64;
wire  b30_1_w78;
wire  b55_1_w79;
wire  b1_0_w80;
wire  b1_1_w81;
wire  b57_0_w82;
wire  b56_0_w83;
wire  b30_0_w84;
wire  b55_3_w85;
wire  b30_3_w67;
wire  b56_3_w68;
wire  b57_3_w86;
wire  b30_2_w65;
wire  b55_0_w87;
wire [3:0] b53_3to0_b59;
wire [3:0] b53_3to0_b54;
wire [3:0] b53_3to0_b60;
wire [3:0] b53_3to0_b61;

assign w0 = RST;
assign b1 = ADRESS;
assign DataOut = b39;
assign b53 = Din;
assign w59 = RW;

assign b39[3] = b39_3;
assign b39[2] = b39_2;
assign b39[1] = b39_1;
assign b39[0] = b39_0;

assign b1_0_w56 = {b1[0]};
assign b1_1_w55 = {b1[1]};
assign b1_1_w69 = {b1[1]};
assign b1_0_w70 = {b1[0]};
assign b1_1_w71 = {b1[1]};
assign b1_0_w72 = {b1[0]};
assign b57_2_w73 = {b57[2]};
assign b56_2_w66 = {b56[2]};
assign b55_2_w74 = {b55[2]};
assign b1_0_w75 = {b1[0]};
assign b1_1_w76 = {b1[1]};
assign b57_1_w77 = {b57[1]};
assign b56_1_w64 = {b56[1]};
assign b30_1_w78 = {b30[1]};
assign b55_1_w79 = {b55[1]};
assign b1_0_w80 = {b1[0]};
assign b1_1_w81 = {b1[1]};
assign b57_0_w82 = {b57[0]};
assign b56_0_w83 = {b56[0]};
assign b30_0_w84 = {b30[0]};
assign b55_3_w85 = {b55[3]};
assign b30_3_w67 = {b30[3]};
assign b56_3_w68 = {b56[3]};
assign b57_3_w86 = {b57[3]};
assign b30_2_w65 = {b30[2]};
assign b55_0_w87 = {b55[0]};
assign b53_3to0_b59[3:0] = {b53[3:0]};
assign b53_3to0_b54[3:0] = {b53[3:0]};
assign b53_3to0_b60[3:0] = {b53[3:0]};
assign b53_3to0_b61[3:0] = {b53[3:0]};

FourbitReg
     s0 (
      .RST(w0),
      .CLK(w59),
      .Ce(w61),
      .Qout(b55),
      .Din(b53));

FourbitReg
     s1 (
      .RST(w0),
      .Qout(b30),
      .Ce(w53),
      .CLK(w59),
      .Din(b53));

FourbitReg
     s3 (
      .RST(w0),
      .Ce(w57),
      .CLK(w59),
      .Qout(b57),
      .Din(b53));

PNU_MUX4
     s4 (
      .o1(b39_0),
      .e1(b1_0_w80),
      .e2(b1_1_w81),
      .i4(b57_0_w82),
      .i3(b56_0_w83),
      .i2(b30_0_w84),
      .i1(b55_0_w87));

PNU_MUX4
     s7 (
      .o1(b39_3),
      .e1(b1_1_w69),
      .e2(b1_0_w70),
      .i1(b55_3_w85),
      .i2(b30_3_w67),
      .i3(b56_3_w68),
      .i4(b57_3_w86));

TTL_AND3
     s11 (
      .Z(w61),
      .A(w60),
      .B(w62),
      .C(w63));

TTL_XOR2
     s12 (
      .Z(w51),
      .B(b1_0_w56),
      .A(b1_1_w55));

TTL_AND2
     s13 (
      .B(w51),
      .Z(w58),
      .A(b1_1_w55));

TTL_AND3
     s16 (
      .A(w54),
      .Z(w57),
      .C(b1_0_w56),
      .B(b1_1_w55));

PNU_ONE
     s15 (
      .o1(w54));

PNU_ONE
     s17 (
      .o1(w60));

PNU_NOT
     s18 (
      .i1(b1_1_w55),
      .o1(w62));

TTL_NOT
     s14 (
      .Z(w53),
      .A(w58));

FourbitReg
     s2 (
      .RST(w0),
      .CLK(w59),
      .Ce(w58),
      .Qout(b56),
      .Din(b53));

PNU_NOT
     s19 (
      .i1(b1_0_w56),
      .o1(w63));

PNU_MUX4
     s5 (
      .o1(b39_1),
      .e1(b1_0_w75),
      .e2(b1_1_w76),
      .i4(b57_1_w77),
      .i3(b56_1_w64),
      .i2(b30_1_w78),
      .i1(b55_1_w79));

PNU_MUX4
     s6 (
      .o1(b39_2),
      .e2(b1_1_w71),
      .e1(b1_0_w72),
      .i4(b57_2_w73),
      .i3(b56_2_w66),
      .i1(b55_2_w74),
      .i2(b30_2_w65));

endmodule

