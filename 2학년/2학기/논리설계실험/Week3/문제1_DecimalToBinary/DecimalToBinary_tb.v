module DecimalToBinary_tb;

wire b0;
wire b1;
wire b2;
wire b3;
reg d0;
reg d1;
reg d2;
reg d3;
reg d4;
reg d5;
reg d6;
reg d7;
reg d8;
reg d9;

decimal_to_binary
 U0 (
  .b0(b0),
  .b1(b1),
  .b2(b2),
  .b3(b3),
  .d0(d0),
  .d1(d1),
  .d2(d2),
  .d3(d3),
  .d4(d4),
  .d5(d5),
  .d6(d6),
  .d7(d7),
  .d8(d8),
  .d9(d9));

  initial
  begin
    d0 = 1'b0;
  end

  initial
  begin
    d1 = 1'b0;
    #100 d1 = 1'b1;
    #100 d1 = 1'b0;
  end

  initial
  begin
    d2 = 1'b0;
    #200 d2 = 1'b1;
    #100 d2 = 1'b0;
  end

  initial
  begin
    d3 = 1'b0;
    #300 d3 = 1'b1;
    #100 d3 = 1'b0;
  end

  initial
  begin
    d4 = 1'b0;
    #400 d4 = 1'b1;
    #100 d4 = 1'b0;
  end

  initial
  begin
    d5 = 1'b0;
    #500 d5 = 1'b1;
    #100 d5 = 1'b0;
  end

  initial
  begin
    d6 = 1'b0;
    #600 d6 = 1'b1;
    #100 d6 = 1'b0;
  end

  initial
  begin
    d7 = 1'b0;
    #700 d7 = 1'b1;
    #100 d7 = 1'b0;
  end

  initial
  begin
    d8 = 1'b0;
    #800 d8 = 1'b1;
    #100 d8 = 1'b0;
  end

  initial
  begin
    d9 = 1'b0;
    #900 d9 = 1'b1;
    #100 d9 = 1'b0;
  end

endmodule
