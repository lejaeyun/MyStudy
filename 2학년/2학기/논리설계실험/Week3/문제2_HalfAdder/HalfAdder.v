module HalfAdder(A,B,S,C);

input A;
input B;
output S;
output C;

wire  w2;
wire  w1;
wire  w3;
wire  w4;

assign w2 = A;
assign w1 = B;
assign S = w4;
assign C = w3;

PNU_XOR2
     s0 (
      .i1(w2),
      .i2(w1),
      .o1(w4));

PNU_AND2
     s1 (
      .i1(w2),
      .i2(w1),
      .o1(w3));

endmodule

