from xlsx import importa

class EntryReader:

    def __init__(self, entry):
        [nn, N, nm, Inc, nc, F, nr, R] = importa(entry)

        self.n_nodes = nn
        self.nodes_matrix = nn
        self.n_members = nm
        self.incidence_matrix = Inc
        self.n_charges = nc
        self.loading_vector = F
        self.n_restrictions = nr
        self.restriction_vector = R

reader = EntryReader("entrada.xlsx")