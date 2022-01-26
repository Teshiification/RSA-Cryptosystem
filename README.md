<h1> RSA EN-& DECRIPTION IN PYTHON (WIP)</h1>

<!-- Language Badges -->
<p align="center">
<a href="https://python.org/" target="Python"> <img src="https://img.icons8.com/color/48/000000/python.png"/> </a>
</p>

<!-- Breafing -->

## Python RSA Encryption

<p>RSA is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977.<a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)">~wiki</a></p>
<p>RSA is also used for todays cryptosystems.</p>

<h2>How it works</h2>
<h3>The Math behind it</h3>
<ul>
    <li>keys: p and q</li>
    <li>n = p * q </li>
    <li>phi = (p-1) * (q-1)</li>
    <li>e = phi + _</li>
    <li>d = extended_euclid(e, phi)</li>
    <li>if n != 0:</li>
    </br>
    <li>Decoded Message = ((message ** e) % n)</li>
    <li>Encoded Message = ((message ** d) % n)</li>
</ul>

<h2>How do I use it?</h2>
<ul>
    <li>Define p and q</li>
    <li>Write: e, d, n = RSA_KeyGenerator(p, q)</li>
    <li>To decode a message: Decode(message, e, n)</li>
    <li>To encode a message: Encode(message, d, n)</li>
</ul>
