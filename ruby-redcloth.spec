%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define		ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby Testing framework
Summary(pl):	Szkielet do testów dla jêzyka Ruby
Name:		ruby-redcloth
Version:	3.0.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/2896/RedCloth-%{version}.tar.gz
# Source0-md5:	eade83d4b1ecc2b415db5e33deb09e05
Source1:	setup.rb
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RedCloth is a module for using Textile in Ruby. Textile is a text format. A very simple text format. Another stab at making readable text that can be converted to HTML.

%prep
%setup -q -n RedCloth-%{version}

%build
cp %{SOURCE1} .
ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

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
