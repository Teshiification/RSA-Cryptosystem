<h1> RSA EN-& DECRIPTION IN PYTHON </h1>

<!-- Language Badges -->
<p align="center">
<a href="https://python.org/" target="Python"> <img src="https://img.icons8.com/color/48/000000/python.png"/> </a>
</p>

<!-- Breafing -->

## Python RSA Encryption

<p>RSA is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.<a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)">~wiki</a></p>
<p>RSA is also used for todays cryptosystems.</p>

<h2>How it works</h2>
<ul>
    <li>insert p and q</li>
    <li>n = p * q </li>
    <li>phi = (p-1) * (q-1)</li>
    <li>e = phi + _</li>
    <li>d = extended_euclid(e, phi)</li>
    <li>if n != 0:</li>
    </br>
    <li>Decoded Message = ((message ** e) % n)</li>
    <li>Encoded Message = ((message ** d) % n)</li>
</ul>
