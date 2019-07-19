import parser
import fabric

def count_overlapped_claims(claims, plan_width, plan_height):
    plan = [[fabric.EMPTY_CELL for _ in range(0, plan_width)] for _ in range(0, plan_height)]
    overlapped_cells_count = 0

    for claim in claims:
        overlapped_cells_count += claim.print_on(plan)

    return overlapped_cells_count


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

print(count_overlapped_claims(claims, max_width, max_height))
