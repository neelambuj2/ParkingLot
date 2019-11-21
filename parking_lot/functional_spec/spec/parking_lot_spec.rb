require 'spec_helper'

RSpec.describe 'Parking Lot' do
  let(:pty) { PTY.spawn('parking_lot') }

  before(:each) do
    run_command(pty, "create_parking_lot 3\n")
  end

  it "can create a parking lot", :sample => true do
    expect(fetch_stdout(pty)).to end_with("Created a parking lot with 3 slots\n")
  end

  it "can park a car" do
    run_command(pty, "park KA-01-HH-3141 Black\n")
    expect(fetch_stdout(pty)).to end_with("Allocated slot number: 1\n")
  end
  
  it "can unpark a car" do
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "leave 1\n")
    expect(fetch_stdout(pty)).to end_with("Slot number 1 is free\n")
  end

  it "test duplicate cars" do
      run_command(pty, "park KA-01-HH-1129 Black\n")
      run_command(pty, "park KA-01-HH-1129 Black\n")
      expect(fetch_stdout(pty)).to end_with("Cars with duplicate registration number cannot be parked\n")
      run_command(pty, "leave 1\n")
  end

  it "test vacating already vacating slots" do
      run_command(pty, "leave 1\n")
      expect(fetch_stdout(pty)).to end_with("This slot is already free\n")
  end

  it "test Parking lot full" do
      run_command(pty, "park KA-01-HH-1129 Black\n")
      run_command(pty, "park KA-01-HH-5555 Black\n")
      run_command(pty, "park KA-01-HH-9999 white\n")
      run_command(pty, "park KA-01-HH-6547 Black\n")
      expect(fetch_stdout(pty)).to end_with("Sorry, parking lot is full\n")
      run_command(pty, "leave 1\n")
      run_command(pty, "leave 2\n")
      run_command(pty, "leave 3\n")
  end

  it "test get slot_number_for_registration_number for unexisiting car" do
      run_command(pty, "slot_number_for_registration_number UNEXIST\n")
      expect(fetch_stdout(pty)).to end_with("Not found\n")
  end

  it "can report status" do
    run_command(pty, "park KA-01-HH-1234 White\n")
    run_command(pty, "park KA-01-HH-3141 Black\n")
    run_command(pty, "park KA-01-HH-9999 White\n")
    run_command(pty, "status\n")
    expect(fetch_stdout(pty)).to end_with(<<-EOTXT
Slot No.    Registration No    Colour
1           KA-01-HH-1234      White
2           KA-01-HH-3141      Black
3           KA-01-HH-9999      White
EOTXT
)
  end

end
