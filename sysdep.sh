apt-get install autotools-dev
apt-get install automake1.9
apt-get install libtool
apt-get install autoconf
apt-get install libncurses-dev
apt-get install xsltproc
apt-get install groff-base
apt-get install libpcre3-dev
apt-get install pkg-config
apt-get install curl
apt-get install lsb-release
curl http://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add -
echo "deb http://repo.varnish-cache.org/debian/ $(lsb_release -s -c) varnish-2.1" >> /etc/apt/sources.list.d/varnish.list
apt-get update
apt-get install varnish
apt-get install haproxy
