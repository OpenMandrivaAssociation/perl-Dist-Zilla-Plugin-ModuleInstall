%define upstream_name    Dist-Zilla-Plugin-ModuleInstall
%define upstream_version 0.02000000

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(inc::Module::Install\\)'
%else
%define _requires_exceptions perl(inc::Module::Install)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Build Module::Install based Distributions with Dist::Zilla
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Role::Tempdir)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)

BuildArch:	noarch

%description
This module will create a _Makefile.PL_ for installing the dist using 
the Module::Install manpage.

It is at present a very minimal feature set, but it works.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


