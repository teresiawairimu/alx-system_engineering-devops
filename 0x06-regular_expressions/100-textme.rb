#!/usr/bin/env ruby

input = ARGV[0]

sender_regex = input.match(/\[from:([^\]]+)\]/)
sender = sender_regex ? sender_regex[1] : nil

receiver_regex = input.match(/\[to:([^\]]+)\]/)
receiver = receiver_regex ? receiver_regex[1] : nil

flags_regex = input.match(/\[flags:([^\]]+)\]/)
flags = flags_regex ? flags_regex[1] : nil

sender = sender[/\+?\d{11}\b/] || sender
receiver = receiver[/\+?\d{11}\b/] || receiver

puts "#{sender},#{receiver},#{flags}"

