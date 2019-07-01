import parser
import fabric

claims = []
max_height = 0
max_width = 0

with open('input.txt') as input_file:
    for input in input_file:
        claim = parser.parse(input)
        claims.append(claim)

        if max_height < claim.height + claim.point.y:
            max_height = claim.height + claim.point.y

        if max_width < claim.width + claim.point.x:
            max_width = claim.width + claim.point.x

plan = [[fabric.EMPTY_CELL for _ in range(0, max_width)] for _ in range(0, max_height)]

for claim in claims:
    claim.print_on(plan)

intact_claims = list(filter(lambda claim: not(claim.is_overlapped or claim.check_if_overlapped_on(plan)), claims))

print(intact_claims[0].id)
