%define upstream_name    Dist-Zilla-Plugin-ModuleInstall
%define upstream_version 0.01054020

%define _requires_exceptions perl(inc::Module::Install)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Build Module::Install based Distributions with Dist::Zilla
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla)
BuildRequires: perl(Dist::Zilla::Role::Tempdir)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module will create a _Makefile.PL_ for installing the dist using the
Module::Install manpage.

It is at present a very minimal feature set, but it works.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*
