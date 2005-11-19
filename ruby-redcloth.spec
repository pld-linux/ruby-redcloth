%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	RedCloth - Textile Humane Web Text for Ruby
Summary(pl):	RedCloth - obs³uga formatu tekstowego dla WWW Textile w jêzyku Ruby
Name:		ruby-redcloth
Version:	3.0.4
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/6064/RedCloth-%{version}.tar.gz
# Source0-md5:	6f076b94e783149adf96102c574a233c
URL:		http://www.whytheluckystiff.net/ruby/redcloth/
BuildRequires: setup.rb
BuildRequires: sed >= 4.0
Requires:	ruby
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RedCloth is a module for using Textile in Ruby. Textile is a text
format. A very simple text format. Another stab at making readable
text that can be converted to HTML.

%description -l pl
RedCloth to modu³ do u¿ywania Textile w Rubym. Textile to format
tekstowy. Bardzo prosty format tekstowy. Kolejny krok do tworzenia
czytelnego tekstu, który mo¿e byæ konwertowany do HTML-a.

%prep
%setup -q -n RedCloth-%{version}
sed -i -e "s#/usr/bin/ruby18#/usr/bin/ruby#" bin/*

%build
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc doc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*
