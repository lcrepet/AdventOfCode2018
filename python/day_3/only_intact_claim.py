import parser
import fabric

def find_only_not_overlapped_claim(claims, plan_width, plan_height):
    plan = [[fabric.EMPTY_CELL for _ in range(0, max_width)] for _ in range(0, max_height)]

    for claim in claims:
        claim.print_on(plan)

    intact_claims = list(filter(lambda claim: not(claim.is_overlapped or claim.check_if_overlapped_on(plan)), claims))

    if (intact_claims):
        return intact_claims[0]


# MAIN SCRIPT

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

not_overlapped_claim = find_only_not_overlapped_claim(claims, max_width, max_height)
if not_overlapped_claim:
    print(not_overlapped_claim.id)
