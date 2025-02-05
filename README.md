To justify the statement that the set of all real \( 2 \times 2 \) matrices forms a four-dimensional real vector space, we need to verify that it satisfies the axioms of a vector space and determine its dimension.

### 1. **Vector Space Axioms**
The set of all \( 2 \times 2 \) real matrices, denoted \( M_{2 \times 2}(\mathbb{R}) \), satisfies the following vector space axioms over the field of real numbers \( \mathbb{R} \):

- **Closure under addition**: If \( A \) and \( B \) are \( 2 \times 2 \) matrices, then \( A + B \) is also a \( 2 \times 2 \) matrix.
- **Closure under scalar multiplication**: If \( A \) is a \( 2 \times 2 \) matrix and \( c \in \mathbb{R} \), then \( cA \) is also a \( 2 \times 2 \) matrix.
- **Associativity of addition**: \( (A + B) + C = A + (B + C) \) for any \( 2 \times 2 \) matrices \( A, B, C \).
- **Commutativity of addition**: \( A + B = B + A \) for any \( 2 \times 2 \) matrices \( A, B \).
- **Existence of a zero vector**: The zero matrix \( \mathbf{0} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} \) acts as the additive identity.
- **Existence of additive inverses**: For any \( 2 \times 2 \) matrix \( A \), the matrix \( -A \) is its additive inverse.
- **Distributivity of scalar multiplication over vector addition**: \( c(A + B) = cA + cB \) for any scalar \( c \in \mathbb{R} \) and matrices \( A, B \).
- **Distributivity of scalar multiplication over scalar addition**: \( (c + d)A = cA + dA \) for any scalars \( c, d \in \mathbb{R} \) and matrix \( A \).
- **Associativity of scalar multiplication**: \( c(dA) = (cd)A \) for any scalars \( c, d \in \mathbb{R} \) and matrix \( A \).
- **Identity element of scalar multiplication**: \( 1 \cdot A = A \) for any \( 2 \times 2 \) matrix \( A \).

Since \( M_{2 \times 2}(\mathbb{R}) \) satisfies all these axioms, it is a vector space over \( \mathbb{R} \).

### 2. **Dimension of the Vector Space**
To determine the dimension of \( M_{2 \times 2}(\mathbb{R}) \), we need to find a basis for this vector space. A basis is a set of linearly independent vectors (matrices, in this case) that span the entire space.

Consider the following four matrices:
\[
E_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad
E_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad
E_3 = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad
E_4 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.
\]

- **Linear Independence**: These matrices are linearly independent because no matrix in the set can be written as a linear combination of the others.
- **Spanning**: Any \( 2 \times 2 \) matrix \( A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) can be expressed as a linear combination of \( E_1, E_2, E_3, E_4 \):
  \[
  A = aE_1 + bE_2 + cE_3 + dE_4.
  \]

Thus, \( \{E_1, E_2, E_3, E_4\} \) is a basis for \( M_{2 \times 2}(\mathbb{R}) \). Since the basis has four elements, the dimension of \( M_{2 \times 2}(\mathbb{R}) \) is 4.

### Conclusion
The set of all real \( 2 \times 2 \) matrices forms a four-dimensional real vector space because it satisfies the vector space axioms and has a basis consisting of four linearly independent matrices.
