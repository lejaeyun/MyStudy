module RippleCarryAdder(A0,B0,S0,A1,B1,S1,A2,B2,S2,A3,B3,S3,C4,C0);

input A0;
input B0;
output S0;
input A1;
input B1;
output S1;
input A2;
input B2;
output S2;
input A3;
input B3;
output S3;
output C4;
input C0;

wire  w3;
wire  w6;
wire  w5;
wire  w8;
wire  w11;
wire  w9;
wire  w10;
wire  w13;
wire  w14;
wire  w16;
wire  w17;
wire  w18;
wire  w19;
wire  w20;
wire  w21;
wire  w22;
wire  w24;
wire  w25;
wire  w26;
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

assign w9 = A0;
assign w10 = B0;
assign S0 = w6;
assign w18 = A1;
assign w19 = B1;
assign S1 = w13;
assign w26 = A2;
assign w27 = B2;
assign S2 = w21;
assign w34 = A3;
assign w35 = B3;
assign S3 = w29;
assign C4 = w31;
assign w3 = C0;

PNU_XOR2
     s0 (
      .o1(w11),
      .i1(w9),
      .i2(w10));

PNU_XOR2
     s1 (
      .i2(w3),
      .o1(w6),
      .i1(w11));

PNU_AND2
     s2 (
      .i1(w3),
      .o1(w5),
      .i2(w11));

PNU_OR2
     s3 (
      .i1(w5),
      .i2(w8),
      .o1(w20));

PNU_AND2
     s4 (
      .o1(w8),
      .i1(w9),
      .i2(w10));

PNU_XOR2
     s5 (
      .o1(w17),
      .i1(w18),
      .i2(w19));

PNU_XOR2
     s6 (
      .o1(w13),
      .i1(w17),
      .i2(w20));

PNU_AND2
     s7 (
      .o1(w14),
      .i2(w17),
      .i1(w20));

PNU_OR2
     s8 (
      .i1(w14),
      .i2(w16),
      .o1(w28));

PNU_AND2
     s9 (
      .o1(w16),
      .i1(w18),
      .i2(w19));

PNU_XOR2
     s10 (
      .o1(w25),
      .i1(w26),
      .i2(w27));

PNU_XOR2
     s11 (
      .o1(w21),
      .i1(w25),
      .i2(w28));

PNU_AND2
     s12 (
      .o1(w22),
      .i2(w25),
      .i1(w28));

PNU_OR2
     s13 (
      .i1(w22),
      .i2(w24),
      .o1(w36));

PNU_AND2
     s14 (
      .o1(w24),
      .i1(w26),
      .i2(w27));

PNU_XOR2
     s15 (
      .o1(w33),
      .i1(w34),
      .i2(w35));

PNU_XOR2
     s16 (
      .o1(w29),
      .i1(w33),
      .i2(w36));

PNU_AND2
     s17 (
      .o1(w30),
      .i2(w33),
      .i1(w36));

PNU_OR2
     s18 (
      .i1(w30),
      .o1(w31),
      .i2(w32));

PNU_AND2
     s19 (
      .o1(w32),
      .i1(w34),
      .i2(w35));

endmodule

