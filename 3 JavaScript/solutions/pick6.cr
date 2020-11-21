def generate_ticket()
    new_ticket = [] of Int32
    (1..6).each do |item|
        new_ticket.push rand(1..99)
    end
    new_ticket
end

def compare_tickets(ticket1, ticket2)
    matches = 0
    ticket1.each_with_index do |value, index|
        matches += 1 if value == ticket2[index]
    end
    matches
end

prizes = [0, 4, 7, 100, 50000, 1000000, 25000000]

winnings = 0
expenses = 0
iter = 0
max_iter = 100000
winning_ticket = generate_ticket()

while (iter < max_iter)
    expenses += 2
    winnings += prizes[compare_tickets(winning_ticket, generate_ticket())]
    iter += 1
end

puts("\nwinnings: #{winnings}\nexpenses: #{expenses}\nroi: #{(winnings - expenses) / expenses}\n\n")



