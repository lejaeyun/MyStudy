module FullAdder(A,B,C,S,Cout);

input A;
input B;
input C;
output S;
output Cout;

wire  w3;
wire  w6;
wire  w5;
wire  w7;
wire  w8;
wire  w11;
wire  w9;
wire  w10;

assign w9 = A;
assign w10 = B;
assign w3 = C;
assign S = w6;
assign Cout = w7;

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
      .o1(w7),
      .i2(w8));

PNU_AND2
     s4 (
      .o1(w8),
      .i1(w9),
      .i2(w10));

endmodule

