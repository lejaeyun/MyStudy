module FourbitReg(RST,CLK,Din,Ce,Qout);

input RST;
input CLK;
input [3:0] Din;
input Ce;
output [3:0] Qout;

wire  w0;
wire  w2;
wire [3:0] b3;
wire [3:0] b7;
wire  w12;
wire  b3_3_w4;
wire  b3_2_w5;
wire  b3_1_w6;
wire  b7_3;
wire  b7_2;
wire  b7_1;
wire  b7_0;
wire  b3_0_w13;

assign w12 = RST;
assign w0 = CLK;
assign b3 = Din;
assign w2 = Ce;
assign Qout = b7;

assign b7[3] = b7_3;
assign b7[2] = b7_2;
assign b7[1] = b7_1;
assign b7[0] = b7_0;

assign b3_3_w4 = {b3[3]};
assign b3_2_w5 = {b3[2]};
assign b3_1_w6 = {b3[1]};
assign b3_0_w13 = {b3[0]};

PNU_DFF_Ce
     s0 (
      .clock(w0),
      .Ce(w2),
      .D(b3_3_w4),
      .Q(b7_3),
      .reset(w12));

PNU_DFF_Ce
     s1 (
      .clock(w0),
      .Ce(w2),
      .D(b3_2_w5),
      .Q(b7_2),
      .reset(w12));

PNU_DFF_Ce
     s2 (
      .clock(w0),
      .Ce(w2),
      .D(b3_1_w6),
      .Q(b7_1),
      .reset(w12));

PNU_DFF_Ce
     s3 (
      .clock(w0),
      .Ce(w2),
      .Q(b7_0),
      .reset(w12),
      .D(b3_0_w13));

endmodule

