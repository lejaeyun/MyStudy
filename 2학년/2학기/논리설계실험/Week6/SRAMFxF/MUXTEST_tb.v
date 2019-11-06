module MUXTEST_tb;

reg [1:0] e;
reg [3:0] i;
wire out;

MUXTEST
 U0 (
  .e(e),
  .i(i),
  .out(out));

  initial
  begin
    e = 2'b00;
    #500 e = 2'b01;
    #500 e = 2'b10;
    #500 e = 2'b11;
  end

  initial
  begin
    i = 4'b1000;
    #100 i = 4'b0100;
    #100 i = 4'b0010;
    #100 i = 4'b0001;
    #100 i = 4'b0000;
    #100 i = 4'b1000;
    #100 i = 4'b0100;
    #100 i = 4'b0010;
    #100 i = 4'b0001;
    #100 i = 4'b0000;
    #100 i = 4'b1000;
    #100 i = 4'b0100;
    #100 i = 4'b0010;
    #100 i = 4'b0001;
    #100 i = 4'b0000;
    #100 i = 4'b1000;
    #100 i = 4'b0100;
    #100 i = 4'b0010;
    #100 i = 4'b0001;
    #100 i = 4'b0000;
  end

endmodule
